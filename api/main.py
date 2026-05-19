import pika, os, sys, threading
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import microservices.analyticsService as analyticsService
import microservices.userNotificationService as userNotificationService
import microservices.clientService as clientService 
import microservices.rentService as rentService

def main():
    threads = [
        threading.Thread(target=userNotificationService.run),
        threading.Thread(target=analyticsService.run),
        threading.Thread(target=clientService.run),
        threading.Thread(target=rentService.run)]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try: 
            sys.exit(0)
        except SystemExit:
            os._exit(0)
