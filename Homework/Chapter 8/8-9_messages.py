def send_messages(unsent_messages,sent_messages):
    while unsent_messages:
      unsent_message = unsent_messages.pop()
      print(f"Sending message: {unsent_message}")
      sent_messages.append(unsent_message)

      
      
def show_sent_messages(sent_messages):
  print("\nThe following messages have been sent:")
  for sent_message in sent_messages:
      print(sent_message)

unsent_messages = ['This is number 1', 'This number number 2', 'This is number 3']
sent_messages = []

send_messages(unsent_messages[:], sent_messages)
show_sent_messages(sent_messages)
print(unsent_messages)
print(sent_messages)