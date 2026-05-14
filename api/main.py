import pika, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import analyticsService, userNotificationService
import clientService, rentService

def main():
    userNotification = UserNotificationService()
    analytics = AnalyticsService()
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
