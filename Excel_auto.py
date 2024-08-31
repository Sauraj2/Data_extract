import tkinter
import pandas as pd       
import tkinter.ttk

fi='CMDB.xlsx'
df=pd.read_excel(fi)
def fetch_data(inpu):
    #fra3pdtawdhrestgwdb3v
    #AMSPDCLD3-cbam195-app1.cbaminternal
    df['CI Name*'] = df['CI Name*'].str.strip().str.lower()
    inpu = inpu.strip().lower()

    # Filter the DataFrame
    filtered_df = df[df['CI Name*'] == inpu][['L1', 'L2','Cloud', 'CI Name*','Tier 1']]
    return filtered_df.to_string(index=False)

root = tkinter.Tk()            
root.geometry('600x700')     
root.title("Welcome to My CMDB app")
def Take_input():
    Output.delete('1.0','end')
    INPUT = inputtxt.get("1.0", "end-1c")
    Output.insert('end', fetch_data(INPUT))
    
l = tkinter.Label(text = "Node name")
inputtxt = tkinter.Text(root, height = 5,
                width = 25,
                bg = "light yellow")

Output = tkinter.Text(root, height = 9, 
              width = 65, 
              bg = "light cyan")

Display = tkinter.Button(root, height = 2,
                 width = 20, 
                 text ="Show",
                 command = lambda:Take_input())
btn = tkinter.Button(root, text = 'Exit !', 
                command = root.destroy) 


btn.pack(side = 'bottom') 

l.pack()
inputtxt.pack()
Display.pack()
Output.pack()

root.mainloop() 
