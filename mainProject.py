from guiProject import *


def main():
    '''
    This function is for calling GUI class created and setting the title and deminisions of the window.
    '''
    window = Tk()
    widgets = GUI(window)
    window.title('XAL Car Insurance Quote')
    window.geometry('400x400')

    window.resizable(False,False)
    window.mainloop()


if __name__ == '__main__':
    main()
