# Imports
import webiopi
webiopi.setDebug()

# Instantiate WebIOPi server
# It starts immediately
#server = webiopi.Server(
   #         port=8000,
   #         login="webiopi",
    #        password="raspberry")

# Retrieve GPIO lib
GPIO = webiopi.GPIO
LED    = 22

RIGHT = 24
LEFT = 17
BOND = 4


# -------------------------------------------------- #
# Macro definition part - Mapped to REST API         #
# -------------------------------------------------- #
# A custom macro which prints out the arg received and return OK
@webiopi.macro
def myMacroWithArgs(arg1, arg2, arg3):
    webiopi.debug("myMacroWithArgs(%s, %s, %s)" % (arg1, arg2, arg3))
    return "OK"

# A custom macro without args which return nothing
@webiopi.macro
def myMacroWithoutArgs():
    webiopi.debug("myMacroWithoutArgs()")


# -------------------------------------------------- #
# Initialization part - WebIOPi will call setup()    #
# -------------------------------------------------- #
def setup():
    # Setup GPIOs
    
    GPIO.setFunction(LED, GPIO.OUT)
   
    GPIO.setFunction(LEFT, GPIO.OUT)
    GPIO.setFunction(RIGHT, GPIO.OUT)
    GPIO.setFunction(BOND, GPIO.OUT)
        
    
   
    
    

# -------------------------------------------------- #
# Loop execution part - WebIOPi will call loop()     #
# -------------------------------------------------- #
# Example loop which toggle RELAY each 5 seconds
def loop():
    GPIO.output(RELAY, not GPIO.input(RELAY))
    webiopi.sleep(5)        

# -------------------------------------------------- #
# Termination part - WebIOPi will call destroy()     #
# -------------------------------------------------- #
def destroy():
    # Reset GPIO functions
    
    GPIO.setFunction(LED, GPIO.IN)

    GPIO.setFunction(LEFT, GPIO.IN)
    GPIO.setFunction(RIGHT, GPIO.IN)
    GPIO.setFunction(BOND, GPIO.IN)
    
