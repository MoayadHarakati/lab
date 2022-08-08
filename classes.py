class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):
        """
        - Create a private variable to store the TV channel. It should be set to the minimum TV channel by default.
        - Create a private variable to store the TV volume. It should be set to the minimum TV volume by default.
        - Create a private variable to store the TV status. The TV should start when it is off.
        """
        self.__channel=Television.MIN_CHANNEL
        self.__volume=Television.MIN_VOLUME
        self.__status=False
        
        

    def power(self):
    
        """
        - This method should be used to turn the TV on/off.
        - If called on a TV object that is off, the TV object should be turned on.
        - If called on a TV object that is on, the TV object should be turned off.
        """
        if self.__status==False:
            self.__status=True
            return True
        if self.__status==True:
            self.__status=False
            return False

    def channel_up(self):
        """
        - This method should be used to adjust the TV channel by incrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MAX_CHANNEL, it should take the TV channel back to the MIN_CHANNEL.
        """
        if self.__status==True:
            if self.__channel==Television.MAX_CHANNEL:
                self.__channel=Television.MIN_CHANNEL
            else:
                self.__channel+=1
        return self.__channel

    def channel_down(self):
        """
        - This method should be used to adjust the TV channel by decrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MIN_CHANNEL, it should take the TV channel back to the MAX_CHANNEL.
        """
        if self.__status==True:
            if self.__channel==Television.MIN_CHANNEL:
                self.__channel=Television.MAX_CHANNEL
            else:
                self.__channel-=1
        return self.__channel

    def volume_up(self):
        """
        - This method should be used to adjust the TV volume by incrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MAX_VOLUME, the volume should not be adjusted.
        """
        if self.__status==True:
            if self.__volume==Television.MAX_VOLUME:
                self.__volume=Television.MAX_VOLUME
            else:
                self.__volume+=1
        return self.__volume
            
                

    def volume_down(self):
        """
        - This method should be used to adjust the TV volume by decrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MIN_VOLUME, the volume should not be adjusted.
        """
        if self.__status==True:
            if self.__volume==Television.MIN_VOLUME:
                self.__volume=Television.MIN_VOLUME
            else:
                self.__volume-=1
        return self.__volume
            
    def __str__(self):
        """
        - This method should be used to return the TV status using the format shown in the comments of main.py
        """
        return f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'

def main():
    # Television 1
    tv_1 = Television()
    tv_1.power()
    print(tv_1)             # TV status: Is on = True, Channel = 0, Volume = 0

    tv_1.channel_up()
    tv_1.channel_up()
    tv_1.volume_up()
    print(tv_1)             # TV status: Is on = True, Channel = 2, Volume = 1

    tv_1.channel_up()
    tv_1.channel_up()
    tv_1.channel_up()
    tv_1.volume_down()
    tv_1.volume_down()
    print(tv_1)             # TV status: Is on = True, Channel = 1, Volume = 0

    # Television 2
    tv_2 = Television()
    tv_2.channel_up()
    tv_2.volume_up()
    print(tv_2)             # TV status: Is on = False, Channel = 0, Volume = 0

    tv_2.power()
    tv_2.channel_up()
    tv_2.volume_up()
    print(tv_2)             # TV status: Is on = True, Channel = 1, Volume = 1

    tv_2.power()
    print(tv_2)             # TV status: Is on = False, Channel = 1, Volume = 1
    tv_2.power()
    tv_2.channel_up()
    print(tv_2)             # TV status: Is on = True, Channel = 2, Volume = 1
    tv_2.volume_up()
    tv_2.volume_up()
    print(tv_2)             # TV status: Is on = True, Channel = 2, Volume = 2


if __name__ == '__main__':
    main()
