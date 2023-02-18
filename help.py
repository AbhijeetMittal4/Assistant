#elif 'the time' or ' what is the time' or 'time' or 'time now' 'time right now' or 'what is the time right now'in query:
#            strTime = datetime.datetime.now().strftime("%H:%M:%S")
#            speak(f"Sir, the time is {strTime}")
#
#
#
#     elif 'search youtube' in query:
#            from bs4 import BeautifulSoup
#
#            textToSearch = takeCommand()
#        
#            query = urllib.parse.quote(textToSearch)
#            url = "https://www.youtube.com/results?search_query=" + query
#            response = urllib.request.urlopen(url)
#            html = response.read()
#            soup = BeautifulSoup(html, 'html.parser')
#            print(soup.findAll(attrs={"class": "yt-uix-tile-link"}))
#
#            for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
#                print('https://www.youtube.com' + vid['href'])
              


import pywhatkit as pyt
pyt.playonyt("pansoori")




#elif 'thank you' or 'thanks' in query:
#       speak(" Your Welcome sir")


elif 'youtube' in query:
            try:
                speak("Trying to open the video waite pls")
                query = query.replace("youtube", "")
                results = pyt.playonyt(query)
            except Exception as e:
                speak("sorry i am dumb and wasn,t able to do the work") 