import pika, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from microservices.analyticsService import AnalyticsService
from microservices.userNotificationService import UserNotificationService
import microservices.clientService as clientService, microservices.rentService as rentService

def main():
    print("Started user notification service")
    userNotification = UserNotificationService()
    print("Started analytics service")
    analytics = AnalyticsService()
    print("Fired events")
    clientService.EventAddUser()
    rentService.EventAddRent()
    rentService.EventFinalizeRent()

try:
    main()
except KeyboardInterrupt:
    print("Interrupted")
    try: 
        sys.exit(0)
    except SystemExit:
        os._exit(0)
