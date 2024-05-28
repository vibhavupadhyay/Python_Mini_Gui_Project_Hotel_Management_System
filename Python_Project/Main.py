def run()->None:
    import Screen_
    Screen_.Screen()

def exi_t()->None:
    f=open("r.s","w")
    f.write("True")
    f.close()
if __name__=="__main__":
    import os
    if os.path.exists("r.s"):
        os.remove("r.s")
    run()