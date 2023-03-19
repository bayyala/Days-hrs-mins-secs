#Write a program that will ask for a number of days and will then show how many hours, minutes and seconds are in that number of days 

yname=input("Enter your name: ")
days=int(input("\nEnter Number of days: "))
hours=days*24 # in a day there are 24 hours
min=hours*60 #in an hour 60 mins
sec=min*60 #in a min 60 secs
print("\n Hi ",yname)
print("\nIn ", days,"days there are...")
print(hours,"hrs")
print(min, " Minutes")
print(sec, " Seconds")