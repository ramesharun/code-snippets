# copy file from local to remote
  1) open terminal on your local machine
  2) cd "/folder /with /the /.pem file/"
  3) scp -i "<FILE_NAME>.pem" "<PATH_TO_LOCAL_FILE>" "<USER>@<REMOTE_IP>:<PATH_TO_LOCAL_FILE>"
     example:
     scp -i "this_is_myFile.pem" "/Users/me/log1.log" "ec2-user@12.345.67.89:/home/ec2-user/log1.log"
     
# copy file from remote to local
  1) open terminal on your local machine
  2) cd "/folder /with /the /.pem file/"
  3) scp -i "<FILE_NAME>.pem" "<USER>@<REMOTE_IP>:<REMOTE_FILE_PATH>"  "<PATH_TO_LOCAL_FILE>"
     example:
     scp -i "this_is_myFile.pem" "ec2-user@12.345.67.89:/home/ec2-user/log1.log" "/Users/me/log1.log"

# copy all folder's files from remote to local
  1) open terminal on your local machine
  2) cd "/folder /with /the /.pem file/"
  3) scp -r -i "<FILE_NAME>.pem" "<USER>@<REMOTE_IP>:<REMOTE_FOLDER_PATH>/"  "<PATH_TO_LOCAL_FOLDER>/"
     example:
     scp -r -i "this_is_myFile.pem" "ec2-user@12.345.67.89:/home/ec2-user/" "/Users/me/"
