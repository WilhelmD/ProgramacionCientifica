from IPython.core.magic import register_cell_magic

@register_cell_magic
def py2_to_py3(line, cell):

    ip = get_ipython()
    
    filename = '_temp.py'
    
    with open(filename, 'w') as f:
        lines = cell.split("\n")
        for line in lines:
            if "print " in line:
                line = line.replace("print ", "print(")
                line += ")"
            line += "\n"
            f.write(line)
    
    output = ip.getoutput('ipython ' + filename)
    
    print('\n'.join(output))
	
def load_ipython_extension(ipython):
       """This function is called when the extension is loaded.
       It accepts an IPython InteractiveShell instance.
       We can register the magic with the `register_magic_function`
       method of the shell instance."""
       ipython.register_magic_function(cpp, 'cell')
