# EP.3 RPA - Auto web browser
'''
launch web browser
go to google.com
type 'keyword'
press enter
capture screen shot
save to file
'''
import webbrowser, time, pyperclip
import pyautogui as p

def Search(keyword, eng=False, scroll=False, scrollamount=10):
    url = 'https://www.google.com'
    webbrowser.open(url)
    time.sleep(3)
    if eng == True:
        p.write(keyword, interval=0.25)
    else:
        pyperclip.copy(keyword)
        time.sleep(1)
        p.hotkey('command','v')
    time.sleep(1)
    p.press('enter')
    time.sleep(2)
    if scroll == True:
        for i in range(scrollamount):
            p.scroll(-100)
            time.sleep(1)
            p.screenshot(f'{i}_{keyword}.png')
            time.sleep(2)
    else:
        p.screenshot(keyword + '.png')

# Search('laos', eng=True)
Search('python programming', eng=True, scroll=True, scrollamount=5)
