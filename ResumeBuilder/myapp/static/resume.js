window.onload = function(){
document.getElementById("button")
    .addEventListener("click",()=>{
       const csk = this.document.getElementById("resume");
       console.log(csk);
       var element = document.getElementById('element-to-print');
       var opt = {
              margin:       1,
              filename:     'myfile.pdf',
              image:        { type: 'jpeg', quality: 0.98 },
              html2canvas:  { scale: 1 },
              jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' }
      };
      html2pdf().from(csk).set(opt).save();
    })
}