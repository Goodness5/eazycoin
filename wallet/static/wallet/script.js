// document.getElementById('button').addEventListener('click',myfun)
function myfunction(){   
    
        document.getElementById('SubmitPayment').style.display = "flex"   


        
}
myfunction();
function wallet(counter) {
        let x = parseInt(document.getElementById('balance').innerHTML);
        let y = (((20/100)*x)+x)
        if(counter === 25){
                return y;
        }     
        setInterval(() => {}, );

}
wallet();
