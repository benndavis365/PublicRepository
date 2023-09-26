def car_info(make, model, **car_details):
  car_details['manufacturer'] = make
  car_details['car_model'] = model
  return car_details


make_car = car_info('subaru', 'outback', color='blue', tow_package=True)
print(make_car)
