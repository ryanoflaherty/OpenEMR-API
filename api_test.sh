#!/bin/bash

WEBPATH="http://52.34.161.30:5000/openemr/api/v0.0/patients"
WEBPATH_AUTH="http://52.34.161.30:5000/openemr/api/v0.1/patients"

pause(){
 read -n1 -rsp $'Press any key to continue...\n'
}

return_all(){
	echo "Checking 'return all' functionality..."
	echo "curl -i $WEBPATH"
	echo "..."
	echo 
	echo "Response from server..."
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
	echo 
	echo "Response from server..."
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
	echo "..."
	echo
	echo "Response from server..."
	curl -i -H "Content-Type: application/json" -X POST -d '{"firstName": "'$firstName'", "lastName":"'$lastName'", "dob":"'$dob'", "height":'$height', "weight":'$weight', "sex":"'$sex'"}' $WEBPATH
	echo
}

update_record(){
	echo "Checking 'update record' functionality..."
	read -n1 -p "Enter Patient ID to update..." key
	echo
	echo "Enter values to update fields. If you do not wish to update, hit enter."
	read -p "Enter first name: " firstName
	read -p "Enter last name: " lastName
	read -p "Enter date of birth: " dob
	read -p "Enter height: " height
	read -p "Enter weight: " weight
	read -p "Enter sex: " sex
	echo "Updating patient record $key..."
	json=""

	if [ "$firstName" != "" ]; then
		json=''$json'"firstName":"'$firstName'",'
	fi
	if [ "$lastName" != "" ]; then
		json=''$json'"lastName":"'$lastName'",'
	fi
	if [ "$dob" != "" ]; then
		json=''$json'"dob":"'$dob'",'
	fi
	if [ "$height" != "" ]; then
		json=''$json'"height":'$height','
	fi
	if [ "$weight" != "" ]; then
		json=''$json'"weight":'$weight','
	fi
	if [ "$sex" != "" ]; then
		json=''$json'"sex":"'$sex'",'
	fi

	if [ "$json" == "" ]; then
		echo "Nothing to update"
	else
		json="${json%?}"
		echo "curl -i -H \"Content-Type: application/json\" -X PUT -d '{$json}' $WEBPATH/$key"
		echo "..."
		echo
		echo "Response from server..."
		curl -i -H "Content-Type: application/json" -X PUT -d '{'$json'}' $WEBPATH/$key
		echo
	fi

	}

delete_record(){
	echo "Checking 'delete record' functionality..."
	read -n1 -r -p "Enter Patient ID to delete..." key
	echo
	echo "Deleting patient record...$key"
	echo "curl -X DELETE $WEBPATH/$key"
	echo "..."
	echo 
	echo "Response from server..."
	curl -X DELETE $WEBPATH/$key
	echo
}

authorization_check(){
	echo "Checking 'user authorization' functionality..."
	echo "Username and password required to view patient records..."
	sleep 1
	read -p "Enter username: " username
	read -p "Enter password: " password
	echo
	echo "curl -u $username:$password -i $WEBPATH_AUTH"
	echo "..."
	echo 
	echo "Response from server..."
	curl -u $username:$password -i $WEBPATH_AUTH
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
	echo "6. Authorization"
	echo "7. Exit"
	echo 
}

get_response(){
	read -n1 -r -p "Enter test number to run..." key
	echo
	if [ "$key" == "" ]
	then
		echo "Please enter a number"
		sleep .5
		print_table
		get_response
	fi
	if [ "$key" != "7" ]; then
		echo "Running test $key..."
	fi
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
	elif [ "$key" -eq "4" ]
	then 
		update_record
	elif [ "$key" -eq "5" ]
	then
		delete_record
	elif [ "$key" -eq "6" ]
	then
		authorization_check
	elif [ "$key" -eq "7" ]
	then
		exit
	fi
	echo

}

echo "==========================================================="
echo "This script will test the functionality of the OpenEMR API."
echo

while true; do
	pause
	print_table
	get_response
done
