
import os.path, sys
from transformers import AutoModelForSeq2SeqLM,AutoTokenizer

model_checkpoint = "razwand/opus-mt-en-mul-finetuned_en_sp_translator"

model = AutoModelForSeq2SeqLM.from_pretrained(model_checkpoint)
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

def translate(line):
    'Using model to translate a line'
    text = tokenizer([line],return_tensors="pt")
    output_text = model.generate(text['input_ids'])
    output = tokenizer.decode(output_text.squeeze(), skip_special_tokens=True)
    return(output)

def write_file(old_line,line, file,type):
    'This function writes the new translated line'
    line = line.replace('Larguin','')
    if type == 't':
        file.write(old_line.replace(old_line,str(line)+"\n"))
    else:
        file.write(old_line.replace(old_line,str(line)))

def check(line,newf):
    '''
    Reads the original files and extract the subtitle text,
    excluding timestamps and the id line        
    '''
    try: 
        num = int(line)
        write_file(line,line,newf,'o')
    except:
        if '->' in line:
            write_file(line,line,newf,'o')
        else:
           string_ = translate(line)
           write_file(line,string_,newf,'t')

def main(file_name):
    '''
    This main function reads the original file and calls the rest of the translation flow to
    write the translated subtitle into the new file with name <file_name>_SP.srt.
    '''
    new_file_name = file_name[:-4] +'_SP'+ '.srt'

    with open('./output/' +new_file_name,'w') as new_file:
            with open('./input/' + file_name, "r") as old_file:
                for line in old_file:
                    check(line,new_file)
def check_args(argv):
    '''
    Function checking input arguments.
    '''
    if len(argv) != 2:
         print('\U0001F4A5 Incorrect number of arguments. Argument should be: name of file')     
    else:
        return(True)

if __name__ == "__main__":

    '''
    This function reads the arguments (file name) and initiates the flow
    
    '''

    if check_args(sys.argv):
        origin_file = sys.argv[1]

        print('------------------------------------------------------')
        print('\U0001F4AB You are about to process {} file'.format(origin_file))
        print('------------------------------------------------------')

        main(origin_file)
    
    else:
        print('\U0001F61E	Processing will not be performed.')
