class RateLimit:
    pass


class GC(RateLimit):
    __CREATE_RATE_LIMIT: int = 600
    __CREATE_GET_BALANCE_GC_LIMIT: int = 50
    __CREATE_CANCEL_GC_LIMIT: int = 50

    @staticmethod
    def post_create_gc(self):
        pass

    @staticmethod
    def post_get_balance_gc(self):
        pass

    @staticmethod
    def post_cancel_gc(self):
        pass


class DigitalIssue(RateLimit):
    @staticmethod
    def delete(self):
        __POST_RATE_LIMIT: int = 900

        pass

    @staticmethod
    def post(self):
        __POST_RATE_LIMIT: int = 50

        pass


class DigitalCheckBalance(RateLimit):
    __POST_RATE_LIMIT: int = 50

    @staticmethod
    def post(self):
        pass


class DigitalOrderStatus(RateLimit):
    __GET_RATE_LIMIT: int = 5000

    @staticmethod
    def get(self):
        pass
