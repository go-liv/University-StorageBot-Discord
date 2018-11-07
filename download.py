#This function allows the user to download a file (it is the last command getting used, before this we have the upload function and a read function)
async def download(ma):
        
        if logged(ma) == True:
            msg = 'Can you tell me the code of the file you want to download?'
            code = await getmsg(ma, msg)
            
            if await checkdb(files, file_code, code):
                file = c.execute(SELECT file_path FROM database WHERE file_code = code AND id = )
                file = open(file)
        
                await client.send_file(ma, file)
                msg = 'You can always download the file by right-clicking the file and using the discord option.' 
                await sendmsg(ma, msg)

        else:
            msg = 'You are not logged in, please log in before trying to download a file'
            await sendmsg(ma, msg)
#
#
#
#         
#
#
#
#
#


