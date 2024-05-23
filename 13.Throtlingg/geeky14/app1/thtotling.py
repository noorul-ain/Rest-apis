# use for child 


from rest_framework.throttling import UserRateThrottle
class JackRate(UserRateThrottle):
    scope = 'jack'
