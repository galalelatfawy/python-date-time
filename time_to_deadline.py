import datetime
import datetime as dt


deadline_input = input("please enter your deadline date in the format task : d.m.y :\n")
input_list = deadline_input.split(":")
task = input_list[0]
task_date = input_list[1]
deadline_date = datetime.datetime.strptime(task_date, "%d.%m.%Y")
today_date = datetime.datetime.today()
time_to_deadline = deadline_date - today_date
print(f"You have a task: **{task}**\n and task deadline is **{task_date}**\n you have {time_to_deadline} "
      f"to finish you task")
