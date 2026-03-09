"""CDP FedCm Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

LoginState = Literal['SignIn','SignUp']
"""Whether this is a sign-up or sign-in action for this account, i.e. whether this account has ever been used to sign in to this RP before."""
DialogType = Literal['AccountChooser','AutoReauthn','ConfirmIdpLogin','Error']
"""The types of FedCM dialogs."""
DialogButton = Literal['ConfirmIdpLoginContinue','ErrorGotIt','ErrorMoreDetails']
"""The buttons on the FedCM dialog."""
AccountUrlType = Literal['TermsOfService','PrivacyPolicy']
"""The URLs that each account has"""
class Account(TypedDict, total=True):
    """Corresponds to IdentityRequestAccount"""
    accountId: str
    email: str
    name: str
    givenName: str
    pictureUrl: str
    idpConfigUrl: str
    idpLoginUrl: str
    loginState: LoginState
    termsOfServiceUrl: NotRequired[str]
    """These two are only set if the loginState is signUp"""
    privacyPolicyUrl: NotRequired[str]