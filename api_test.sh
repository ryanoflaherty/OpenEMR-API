#!/bin/bash

WEBPATH="http://52.32.30.227:5000/openemr/api/v0.0/patients"

pause(){
 read -n1 -rsp $'Press any key to continue...\n'
}

return_all(){
	echo "Checking 'return all' functionality..."
	echo "curl -i $WEBPATH"
	echo "..."
	curl -i $WEBPATH
	echo
}

return_one(){
	echo "Checking 'return one' functionality..."
	read -n1 -p "Enter Patient ID to check..." key
	echo
	echo "Returning patient record...$key"
 	echo "curl -i $WEBPATH/$key"
	echo "..."
	curl -i $WEBPATH/$key
	echo
}

create_record(){
	echo "Checking 'create record' functionality..."
	echo
	read -p "Enter first name : " firstName
	read -p "Enter last name : " lastName
	read -p "Enter date of birth: " dob
	read -p "Enter height: " height
	read -p "Enter weight: " weight
	read -p "Enter sex: " sex
	echo "Creating patient record..."
	echo "curl -i -H \"Content-Type: application/json\" -X POST -d '{\"firstName\":\"$firstName\", \"lastName\":\"$lastName\", \"dob\":\"$dob\", \"height\":\"$height\", \"weight\":\"$weight\", \"sex\":\"$sex\"}' $WEBPATH"
	curl -i -H "Content-Type: application/json" -X POST -d '{"firstName": "'$firstName'", "lastName":"'$lastName'", "dob":"'$dob'", "height":'$height', "weight":'$weight', "sex":"'$sex'"}' $WEBPATH

}

update_record(){
	echo
}

delete_record(){
	echo "Checking 'delete record' functionality..."
	read -n1 -r -p "Enter Patient ID to delete..." key
	echo
	echo "Deleting patient record...$key"
	echo "curl -X DELETE $WEBPATH/$key"
	echo "..."
	curl -X DELETE $WEBPATH/$key
	echo
}

print_table(){
	echo
	echo "========== Table of Contents ========="
	echo "1. Return all records"
	echo "2. Return one record"
	echo "3. Create record"
	echo "4. Update record"
	echo "5. Delete record"
	echo 
}

get_response(){
	read -n1 -r -p "Enter test number to run..." key
	echo
	echo "Running test $key..."
	sleep .5

	if [ "$key" -eq "1" ]
	then
		return_all
	elif [ "$key" -eq "2" ]
	then 
		return_one
	elif [ "$key" -eq "3" ]
	then 
		create_record
	elif [ "$key" -eq "5" ]
	then
		delete_record
	fi
	echo

}

# Script starts here
echo "==========================================================="
echo "This script will test the functionality of the OpenEMR API."
echo

while true; do
	pause
	print_table
	get_response
done
