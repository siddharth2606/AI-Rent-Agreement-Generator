const API="http://127.0.0.1:8000";

async function generateAgreement(){

const data={

landlord_name:document.getElementById("landlord_name").value,

tenant_name:document.getElementById("tenant_name").value,

property_address:document.getElementById("property_address").value,

monthly_rent:Number(document.getElementById("monthly_rent").value),

security_deposit:Number(document.getElementById("security_deposit").value),

start_date:document.getElementById("start_date").value,

end_date:document.getElementById("end_date").value

};

try{

const response=await axios({

url:`${API}/generate`,

method:"POST",

data:data,

responseType:"blob"

});

const url=window.URL.createObjectURL(response.data);

const a=document.createElement("a");

a.href=url;

a.download="RentAgreement.pdf";

document.body.appendChild(a);

a.click();

a.remove();

window.URL.revokeObjectURL(url);

alert("Agreement Generated Successfully");

}

catch(err){

console.log(err);

alert("Something went wrong");

}

}