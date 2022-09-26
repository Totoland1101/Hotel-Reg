from tkinter import *

class Application(Frame):
	def __init__(self,master):
		Frame.__init__(self,master)
		self.grid()
		self.create_widget()
	
	def create_widget(self):
		self.main_lbl=Label(self,text="\t\t\t\t\t\tWELCOME TO THE RESTAURANT")
		self.main_lbl.grid(row=0,column=0,columnspan=2,sticky=W)
		
		self.sec_lbl=Label(self,text="\t\t\t\t\t\t\tMenu").grid(row=1,column=0,columnspan=3,sticky=W)
		
		self.starter_lbl=Label(self,text="Starters")
		self.starter_lbl.grid(row=2,column=0,columnspan=3,sticky=W)

		self.starter_lbl=Label(self,text="Name")
		self.starter_lbl.grid(row=3,column=0,columnspan=3,sticky=W)
	
		self.starter_lbl=Label(self,text="Rate per Quantity")
		self.starter_lbl.grid(row=3,column=1,columnspan=3,sticky=W)

		self.starter_lbl=Label(self,text="Quantity")
		self.starter_lbl.grid(row=3,column=2,columnspan=3,sticky=W)

		

		self.crm_tmto=BooleanVar()
		Checkbutton(self,text="Cream Of Tomato",variable=self.crm_tmto).grid(row=4,column=0,sticky=W)
		
		self.sec_lbl=Label(self,text="80").grid(row=4,column=1,columnspan=3,sticky=W)	

		self.crm_tmto_value=Entry(self)
		self.crm_tmto_value.grid(row=4,column=2,sticky=W)

		self.chic_gouj=BooleanVar()
		Checkbutton(self,text="Chicken Goujon",variable=self.chic_gouj).grid(row=5,column=0,sticky=W)

		self.sec_lbl=Label(self,text="100").grid(row=5,column=1,columnspan=3,sticky=W)
		
		self.chic_gouj_value=Entry(self)
		self.chic_gouj_value.grid(row=5,column=2,sticky=W)	

		self.fish_gouj=BooleanVar()
		Checkbutton(self,text="Fish Goujon",variable=self.fish_gouj).grid(row=6,column=0,sticky=W)

		self.sec_lbl=Label(self,text="120").grid(row=6,column=1,columnspan=3,sticky=W)
		
		self.fish_gouj_value=Entry(self)
		self.fish_gouj_value.grid(row=6,column=2,sticky=W)			
	
		self.main_crs_lbl=Label(self,text="Main Course")
		self.main_crs_lbl.grid(row=8,column=0,columnspan=2,sticky=W)

		self.starter_lbl=Label(self,text="Name")
		self.starter_lbl.grid(row=9,column=0,columnspan=3,sticky=W)
	
		self.starter_lbl=Label(self,text="Rate per Quantity")
		self.starter_lbl.grid(row=9,column=1,columnspan=3,sticky=W)

		self.starter_lbl=Label(self,text="Quantity")
		self.starter_lbl.grid(row=9,column=2,columnspan=3,sticky=W)
		
		self.sphag=BooleanVar()
		Checkbutton(self,text="Spaghetti With Tomato,Black Olives and Capers",variable=self.sphag).grid(row=10,column=0,sticky=W)
		
		self.sec_lbl=Label(self,text="310").grid(row=10,column=1,columnspan=3,sticky=W)

		self.sphag_value=Entry(self)
		self.sphag_value.grid(row=10,column=2,sticky=W)	

		self.chic_tmto=BooleanVar()
		Checkbutton(self,text="Chicken With Tomato & Peppers",variable=self.chic_tmto).grid(row=11,column=0,sticky=W)
		
		self.sec_lbl=Label(self,text="270").grid(row=11,column=1,columnspan=3,sticky=W)

		self.chic_tmto_value=Entry(self)
		self.chic_tmto_value.grid(row=11,column=2,sticky=W)	

		self.lamb=BooleanVar()
		Checkbutton(self,text="Lamb Stroganoff",variable=self.lamb).grid(row=12,column=0,sticky=W)

		self.sec_lbl=Label(self,text="370").grid(row=12,column=1,columnspan=3,sticky=W)
		
		self.lamb_value=Entry(self)
		self.lamb_value.grid(row=12,column=2,sticky=W)	

		self.chic_la=BooleanVar()
		Checkbutton(self,text="Chicken Al La King",variable=self.chic_la).grid(row=13,column=0,sticky=W)

		self.sec_lbl=Label(self,text="290").grid(row=13,column=1,columnspan=3,sticky=W)
		
		self.chic_la_value=Entry(self)
		self.chic_la_value.grid(row=13,column=2,sticky=W)	

		self.pasta=BooleanVar()
		Checkbutton(self,text="Pasta With Bechamel Sauce",variable=self.pasta).grid(row=14,column=0,sticky=W)

		self.sec_lbl=Label(self,text="240").grid(row=14,column=1,columnspan=3,sticky=W)
		
		self.pasta_value=Entry(self)
		self.pasta_value.grid(row=14,column=2,sticky=W)	
		
		self.dessert_lbl=Label(self,text="Desserts")
		self.dessert_lbl.grid(row=16,column=0,columnspan=3,sticky=W)

		self.starter_lbl=Label(self,text="Name")
		self.starter_lbl.grid(row=17,column=0,columnspan=3,sticky=W)
	
		self.starter_lbl=Label(self,text="Rate per Quantity")
		self.starter_lbl.grid(row=17,column=1,columnspan=3,sticky=W)

		self.starter_lbl=Label(self,text="Quantity")
		self.starter_lbl.grid(row=17,column=2,columnspan=3,sticky=W)

		self.doub_choc=BooleanVar()
		Checkbutton(self,text="Double Chocolate Cake",variable=self.doub_choc).grid(row=18,column=0,sticky=W)

		self.sec_lbl=Label(self,text="70").grid(row=18,column=1,columnspan=3,sticky=W)
		
		self.doub_choc_value=Entry(self)
		self.doub_choc_value.grid(row=18,column=2,sticky=W)

		self.cheesecake=BooleanVar()
		Checkbutton(self,text="CheeseCake",variable=self.cheesecake).grid(row=19,column=0,sticky=W)

		self.sec_lbl=Label(self,text="60").grid(row=19,column=1,columnspan=3,sticky=W)
		
		self.cheesecake_value=Entry(self)
		self.cheesecake_value.grid(row=19,column=2,sticky=W)

		self.choc_brw=BooleanVar()
		Checkbutton(self,text="Chocolate Brownies",variable=self.choc_brw).grid(row=20,column=0,sticky=W)

		self.sec_lbl=Label(self,text="75").grid(row=20,column=1,columnspan=3,sticky=W)
		
		self.choc_brw_value=Entry(self)
		self.choc_brw_value.grid(row=20,column=2,sticky=W)

		self.rice_pudd=BooleanVar()
		Checkbutton(self,text="Rice Pudding",variable=self.rice_pudd).grid(row=21,column=0,sticky=W)

		self.sec_lbl=Label(self,text="85").grid(row=21,column=1,columnspan=3,sticky=W)
		
		self.rice_pudd_value=Entry(self)
		self.rice_pudd_value.grid(row=21,column=2,sticky=W)

		#self.done_bttn=BooleanVar()
		Button(self,text="DONE!",command=self.reveal).grid(row=22,column=1,columnspan=2,sticky=W)

		self.totpric=Text(self,width=100,height=100,wrap=WORD)
		self.totpric.grid(row=23,column=0,columnspan=2,sticky=W)

		

	def reveal(self):
		Price=0
		content=""
		if self.crm_tmto.get():
			Price=Price+(int(self.crm_tmto_value.get())*60)
			message1="Cream Of Tomato : %dX60\n"%(int(self.crm_tmto_value.get()))	
			content=content+message1

		if self.chic_gouj.get():
			Price=Price+(int(self.chic_gouj_value.get())*100)
			message1="Chicken Goujon : %dX100\n"%(int(self.chic_gouj_value.get()))	
			content=content+message1

		if self.fish_gouj.get():
			Price=Price+(int(self.fish_gouj_value.get())*120)
			message1="Fish Goujon : %dX120\n"%(int(self.fish_gouj_value.get()))	
			content=content+message1

		if self.sphag.get():
			Price=Price+(int(self.sphag_value.get())*310)
			message1="Spaghetti with Tomato,Black Olives and Capers : %dX310\n"%(int(self.sphag_value.get()))	
			content=content+message1

		if self.chic_tmto.get():
			Price=Price+(int(self.chic_tmto_value.get())*270)
			message1="Chicken with Tomato & Peppers : %dX270\n"%(int(self.chic_tmto_value.get()))	
			content=content+message1

		if self.lamb.get():
			Price=Price+(int(self.lamb_value.get())*370)
			message1="Lamb Stroganoff : %dX370\n"%(int(self.lamb_value.get()))	
			content=content+message1

		if self.chic_la.get():
			Price=Price+(int(self.chic_la_value.get())*290)
			message1="Chicken Al La King : %dX290\n"%(int(self.chic_la_value.get()))	
			content=content+message1

		if self.pasta.get():
			Price=Price+(int(self.pasta_value.get())*240)
			message1="Pasta With Bechamel Sauce : %dX240\n"%(int(self.pasta_value.get()))	
			content=content+message1

		if self.doub_choc.get():
			Price=Price+(int(self.doub_choc_value.get())*70)
			message1="Double Chocolate Cake : %dX70\n"%(int(self.doub_choc_value.get()))	
			content=content+message1

		if self.cheesecake.get():
			Price=Price+(int(self.cheesecake_value.get())*60)
			message1="CheeseCake : %dX60\n"%(int(self.cheesecake_value.get()))	
			content=content+message1

		if self.choc_brw.get():
			Price=Price+(int(self.choc_brw_value.get())*75)
			message1="Chocolate Brownies : %dX75\n"%(int(self.choc_brw_value.get()))	
			content=content+message1

		if self.rice_pudd.get():
			Price=Price+(int(self.rice_pudd_value.get())*85)
			message1="Rice Pudding : %dX85\n"%(int(self.rice_pudd_value.get()))	
			content=content+message1

		message="YOUR TOTAL BILL = %d\n\t\tTHANK YOU\n\t\tVISIT AGAIN"%(Price)
		self.totpric.delete(0.0,END)
		message=content+message
		self.totpric.insert(0.0,message)		

root=Tk()
root.title("Restaurant")
root.geometry("750x600")
app=Application(root)
root.mainloop()