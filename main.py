from booking.bookings import Booking

'''
inst=Booking()
inst.land_first_page() 
'''

with Booking() as bot:
    bot.land_first_page() # as we get out of with __exit__() is called
    #bot.change_currency() # can only select 'suggested for you' currency if given args bcz 'all currencies' have diff html
    bot.select_place('Lahore')
    bot.select_date()
    bot.select_adults(5)
    bot.search()
    bot.apply_filtrations()