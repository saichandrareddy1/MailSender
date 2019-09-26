# MailSender
This mainly used for to send accuracy, epochs to your mail 


This is used for Deep learning Engineers Mainly because every one need to know about the accuracy of validation and train datasets when they are training for CNN 


#THIS CODE WILL HELP YOU HOW TO USE IN YOUR CASE####

	epochs = 10
	num = int(input("INFO[] ENTER NUMBER WHICH YOU NEED TO DIVIDE:-"))
	for epoch in range(epochs):
		history = model.fit_generator(train_generator, steps_per_epoch = 1,
		epochs=1, validation_data=validation_generator,validation_steps = 1, verbose=1)


		if (epoch)%num == 0:
			val_acc = history.history['val_acc']
			val_acc = val_acc[-1]
			acc = history.history['acc']
			acc = acc[-1]
			
			#Parameters
			mail = MailSender("Message", "Sender_mail@gmail.com", "password", "Reciver_mail@gmail.com", 47, val_acc, acc, epoch, num) 
			#Function Call
			mail.mailsend()
			
			
			
Requirements

	pip3 install secure-smtplib
	pip3 install python-time
	

How to attach to your System

#ubuntu

	git clone https://github.com/saichandrareddy1/MailSender.git
	
#for windows

	down load it from https://github.com/saichandrareddy1/MailSender.git
	
Keep this file in your CNN model directory

Import method 

	import Mail

Thanks
	
