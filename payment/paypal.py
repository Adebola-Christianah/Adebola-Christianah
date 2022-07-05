import sys 

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AY98XE05KeF9QGzInYMF_TE3mEpm9gCVKRCkIGVPntnYwiv_Ks49OnPcCg3UQh1xjOqjHdrR65R0LzDn"
        self.client_secret = "EOAF2xvYJfwrmTTsEpNNViScdAWloc7v_fpv5BRd0QBPbYde8Lwt6HzxlOVm1tVSlmkrHvCp6jqrfrHd"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
