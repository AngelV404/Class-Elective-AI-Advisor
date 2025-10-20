import os
from typing import Dict, Any, Optional
from .auth_provider import AuthProvider, AuthError, validate_email_domain

import boto3
from botocore.exceptions import ClientError


class CognitoAuthProvider(AuthProvider):
    def __init__(self):
        self.region = os.getenv("AWS_REGION")
        self.user_pool_id = os.getenv("COGNITO_USER_POOL_ID")
        self.client_id = os.getenv("COGNITO_CLIENT_ID")
        if not (self.region and self.user_pool_id and self.client_id):
            raise RuntimeError("Set AWS_REGION, COGNITO_USER_POOL_ID, COGNITO_CLIENT_ID in environment.")
        self.client = boto3.client("cognito-idp", region_name=self.region)

    # ----- helpers -----
    @staticmethod
    def _err(e: ClientError) -> str:
        data = e.response.get("Error", {})
        return f"{data.get('Code','CognitoError')}: {data.get('Message', str(e))}"

    # ----- required by AuthProvider -----
    def register_user(self, full_name: str, email: str, password: str) -> Dict[str, Any]:
        # app-side domain enforcement
        err = validate_email_domain(email)
        if err:
            raise AuthError(err)

        try:
            resp = self.client.sign_up(
                ClientId=self.client_id,
                Username=email,
                Password=password,
                UserAttributes=[
                    {"Name": "email", "Value": email},
                    {"Name": "name", "Value": full_name},
                ],
            )
            # user must confirm via code before login will succeed (unless auto-confirm is enabled)
            return {"cognito": resp, "message": "A verification code was sent to your email."}
        except ClientError as e:
            raise AuthError(self._err(e))

    def authenticate_user(self, email: str, password: str) -> Dict[str, Any]:
        try:
            resp = self.client.initiate_auth(
                ClientId=self.client_id,
                AuthFlow="USER_PASSWORD_AUTH",
                AuthParameters={"USERNAME": email, "PASSWORD": password},
            )
            tokens = resp.get("AuthenticationResult", {})
            # Optional: enrich with attributes
            info = {"email": email, "full_name": None}
            try:
                u = self.get_user_by_email(email)
                if u and "attributes" in u:
                    info["full_name"] = u["attributes"].get("name")
            except Exception:
                pass
            return {"user": info, "tokens": tokens}
        except ClientError as e:
            raise AuthError(self._err(e))

    def get_user_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        try:
            resp = self.client.list_users(
                UserPoolId=self.user_pool_id,
                Filter=f'email = "{email}"',
                Limit=1,
            )
            users = resp.get("Users", [])
            if not users:
                return None
            u = users[0]
            attrs = {a["Name"]: a["Value"] for a in u.get("Attributes", [])}
            return {"username": u.get("Username"), "attributes": attrs, "status": u.get("UserStatus")}
        except ClientError as e:
            raise AuthError(self._err(e))

    # ----- extra desktop-friendly actions -----
    def confirm_sign_up(self, email: str, code: str) -> None:
        try:
            self.client.confirm_sign_up(ClientId=self.client_id, Username=email, ConfirmationCode=code)
        except ClientError as e:
            raise AuthError(self._err(e))
        
    def resend_confirmation(self, email: str) -> None:
        try:
            self.client.resend_confirmation_code(ClientId=self.client_id, Username=email)
        except ClientError as e:
            raise AuthError(self._err(e))


    
