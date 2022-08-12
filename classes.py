class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel 

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) ->None:
        """
        This constructor is for intiating the status, volume, channel of the TV,
        """
        self.__channel=Television.MIN_CHANNEL
        self.__volume=Television.MIN_VOLUME
        self.__status=False

    def power(self) ->bool:
    
        """
        - This method should be used to turn the TV on/off.
        """
        if self.__status==False:
            self.__status=True
        if self.__status==True:
            self.__status=False

    def channel_up(self) -> int:
        """
        - This method should be used to adjust the TV channel by incrementing its value.
        """
        if self.__status==True:
            if self.__channel==Television.MAX_CHANNEL:
                self.__channel=Television.MIN_CHANNEL
            else:
                self.__channel+=1

    def channel_down(self) -> int:
        """
        - This method should be used to adjust the TV channel by decrementing its value.
        """
        if self.__status==True:
            if self.__channel==Television.MIN_CHANNEL:
                self.__channel=Television.MAX_CHANNEL
            else:
                self.__channel-=1

    def volume_up(self) -> int:
        """
        - This method should be used to adjust the TV volume by incrementing its value.
        """
        if self.__status==True:
            if self.__volume==Television.MAX_VOLUME:
                self.__volume=Television.MAX_VOLUME
            else:
                self.__volume+=1

    def volume_down(self) -> int:
        """
        - This method should be used to adjust the TV volume by decrementing its value.
        """
        if self.__status==True:
            if self.__volume==Television.MIN_VOLUME:
                self.__volume=Television.MIN_VOLUME
            else:
                self.__volume-=1
            
    def __str__(self) -> str:
        """
        - This method should be used to return the TV status using the format shown in the comments of main.py
        :return: String containing the status, volume, and channel of the TV.
        """
        return f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'


