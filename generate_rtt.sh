#!/bin/bash

helpFunction()
{
   echo ""
   echo "Usage: $0 -c count -d destination"
   echo -e "\t-c ping count"
   echo -e "\t-d destination address"
   exit 1
}

while getopts "c:d:" opt
do
   case "$opt" in
      c ) count="$OPTARG" ;;
      d ) destination="$OPTARG" ;;
      ? ) helpFunction ;; # Print helpFunction in case parameter is non-existent
   esac
done

# Print helpFunction in case parameters are empty
if [ -z "$count" ] || [ -z "$destination" ]
then
   echo "Some or all of the parameters are empty";
   helpFunction
fi

echo "Sending $count packets..."
filename="./rtt_log/$(date +"%Y_%m_%d_%I_%M_%p").log"
ping -c $count $destination | sed -rn 's|.*=([0-9]+\.?[0-9]+?) ms|\1|p' > $filename
echo "Generating plot"
./make_plot.py $filename
