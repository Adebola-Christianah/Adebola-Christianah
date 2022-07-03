document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.datepicker');
    var options = {'yearRange':20,"format":'yyyy-mm-dd'}
    var instances = M.Datepicker.init(elems,options);
});
console.log('hello world')
const whenb=document.querySelectorAll('.when')
const countdown=document.querySelectorAll('.countsdown')

    
        
           
        setInterval(()=>{
            
                for(var i=0;i<countdown.length;i++){
                    for(j=0;j<whenb.length;j++){
                        const date=Date.parse(whenb[j].textContent)
                        const now=new Date().getTime()
                        const diff=date-now
                        const d=Math.floor(diff/(1000*60*60*24))
                        const h=Math.floor((diff/(1000*60*60))%24)
                        const m=Math.floor((diff/(1000*60))%60)
                        const s=Math.floor((diff/(1000))%60)
                        if(diff>=0){
                            countdown[j].innerHTML=d+"day(s), "+h+"hour(s), "+m+"minute(s), "+s+"second(s)"
                        }elif(diff<-1){
                            countdown[j].innerHTML="Task overdue"
                        }
                       
                }
            }
            },1000)
            
        
    
    

console.log(whenb)
console.log(countdown)


       



    



       
         
    
  