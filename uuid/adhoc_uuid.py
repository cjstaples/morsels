import uuid

my_uuid = uuid.uuid4()
my_uuid_as_string = str(my_uuid)
my_uuid_from_string = uuid.UUID(my_uuid_as_string)

print('UUID  str():  ' + str(my_uuid))
print('UUID as str:  ' + my_uuid_as_string)

assert my_uuid == my_uuid_from_string
