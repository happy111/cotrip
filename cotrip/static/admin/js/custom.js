$(document).ready(function()
{
  base_id = $("#base_admin_id").val();
  login_home = "http//:"+base_id+"/admin/";
  c_location = "http//:"+base_id+String(window.location.pathname);

  if(login_home == c_location)
  {
       window.location.href = "/mis_admin/";
    }
   //admin/billmanagement/billauthentication/

  base_admin_id = "http//:"+base_id+"/admin/billmanagement/billauthentication/";

  c_location = "http//:"+base_id+String(window.location.pathname);

  
  if(base_admin_id == c_location)
  {
       window.location.href = "/mis_admin/billmanagement/";
  }

  // For Bill Management
  $('.model-billauthentication').find("#searchbar")
  .attr('title', "Search by Restaurant name, Mobile Number, Email")
  // For Contact Us Management
   $('.model-contactdetails').find("#searchbar")
  .attr('title', "Search by Name, Mobile Number, Email")
  // For Cashy Customer Wallet Management
   $('.model-cashycustomerwallet').find("#searchbar")
  .attr('title', "Search by Name, Mobile Number, Email")
  // For Cashy Customer Reedem Management
   $('.model-cashyuserredeem').find("#searchbar")
  .attr('title', "Search by Name, Mobile Number, Email, Reedem Brand Name")
  // For Actual wallet coins Management
   $('.model-actualwalletcoins').find("#searchbar")
  .attr('title', "Search by Name,  Mobile Number,  Email,  Exact coins")
  // For Resturant Menu  Management
   $('.model-resturantmenu').find("#searchbar")
  .attr('title', "Search by Menu Name, Resturant Name, cuisine, description, Amount")
  // For Reservation  Managemen
   $('.model-reservation').find("#searchbar")
  .attr('title', "Search by Name, Email, Resturant Name")
  // For Reservation  Management
   $('.model-menuimages').find("#searchbar")
  .attr('title', "Search by Resturant Name")


  // For Restaurant User  Management

   $('.model-restaurantuser').find("#searchbar")
  .attr('title', "Search by Name, Mobile Number, Email")



  //  search_fields = ['restaurant_name','feature','latitude','longitude','restaurant_address','cuisine']

   $('.model-restaurantdetails').find("#searchbar")
  .attr('title', "Search by Restaurant Name, Restaurant address, Email ID, Commission")



 // For Restaurant Branch  Management

   $('.model-resturantbranch').find("#searchbar")
  .attr('title', "Search by Restaurant Name, Email, Branch Name")



 // For Refer A Friend  Management

   $('.model-refercode').find("#searchbar")
  .attr('title', "Search by Name, Email, Mobile Number")



 // For Rating  Management
 
   $('.model-ratingrecord').find("#searchbar")
  .attr('title', "Search by Name, Email, Mobile Number, Restaurant Name")


   // For Cashe User Payment  Management
   
   $('.model-cashyuserpayment').find("#searchbar")
  .attr('title', "Search by Transaction ID, Name, Email, Mobile, Amount")

   // For Cashe User Payment  Management
   
   $('.model-notificationrecord').find("#searchbar")
  .attr('title', "Search by Name, Content")


   // For Cashy Invoice  Management
   
   $('.model-cashyinvoice').find("#searchbar")
  .attr('title', "Search by Restaurant Name, Invoice Number")


   // For Cashy Food Customer  Management
   
   $('.model-cashyfoodcustomer').find("#searchbar")
  .attr('title', "Search by User Name, Email, Mobile")



   // For OTP  Management
   
   $('.model-cashyuserotp').find("#searchbar")
  .attr('title', "Search by User Name, Email")


  // For Currency  Management
   
   $('.model-currencymaster').find("#searchbar")
  .attr('title', "Search by Currency, Symbol, Code ISO")

    // For Language  Management
   
   $('.model-language').find("#searchbar")
  .attr('title', "Search by Language Name, Language Code")


    // For Coins To Currency  Management
    $('.model-coinstocurrency').find("#searchbar")
  .attr('title', "Search by Cashyfood Coins")

     // For Commission Parameter  Management
    $('.model-comissionparameter').find("#searchbar")
  .attr('title', "Search by Commission Mode,  Subscription Plan")


     // For Mode  Management
    $('.model-comissionmode').find("#searchbar")
  .attr('title', "Search by Commission Mode")

     // For Redeem Brand  Management
    $('.model-redeembrandmaster').find("#searchbar")
  .attr('title', "Search by Redeem Brand Name")

      // For Country Management
    $('.model-countrymaster').find("#searchbar")
  .attr('title', "Search by  Country, Currency")
      // For State Management
    $('.model-statemaster').find("#searchbar")
  .attr('title', "Search by State")


    // For City Management
    $('.model-citymaster').find("#searchbar")
  .attr('title', "Search by City")

    // For District Management
    $('.model-districtmaster').find("#searchbar")
  .attr('title', "Search by District")


      // For Subdistrict Management
    $('.model-subdistrictmaster').find("#searchbar")
  .attr('title', "Search by Subdistrict")

        // For Motification Management
    $('.model-notificationconfiguration').find("#searchbar")
  .attr('title', "Search by Notification Type, Description")



    // For Customer Credit (Wallet Management)
    $('.model-customercredit').find("#searchbar")
  .attr('title', "Search Name, Email ID, Mobile")




    // For Customer Credit (Restruant Service Management)
    $('.model-servicemaster').find("#searchbar")
  .attr('title', "Search by Service Name")


    // For Customer Credit (Restruant Service Management)
    $('.model-cashyfoodgoldcustomer').find("#searchbar")
  .attr('title', "Search by Name, Email, Mobile, Plan Type")


      $('.model-cashyfoodregularcustomer').find("#searchbar")
  .attr('title', "Search by Name, Email, Mobile")


    $('.model-restaurantmilesrules').find("#searchbar")
  .attr('title', "Search by Rule Name")


     $('.filtered').find("#cc")
  .attr('title', "Search by Restaurant Name")



    $('.model-attribute ').find("#searchbar")
  .attr('title', "Search by Attribute Name")


    $('.menu-pinned').find("#srname")
  .attr('title', "Search by Restaurant Name")


     $('.model-customergiftvoucher').find("#searchbar")
  .attr('title', "Search by Provider, Product ID")

    $('.model-redemptiongiftvoucherrecords').find("#searchbar")
  .attr('title', "Search by Provider, User Name")





$("#company_form").submit(function () {
$(".default").attr("disabled", true);
return true;
});


$("#subscriptionplan_form").submit(function () {
$(".default").attr("disabled", true);
return true;
});



$("#subscriptionplantype_form").submit(function () {
$(".default").attr("disabled", true);
return true;
});



$("#currencymaster_form").submit(function () {
$(".default").attr("disabled", true);
return true;
});


$("#language_form").submit(function () {
$(".default").attr("disabled", true);
return true;
});


$("#coinstocurrency_form").submit(function () {
$(".default").attr("disabled", true);
return true;
});


$("#comissionparameter_form").submit(function () {
$(".default").attr("disabled", true);
return true;
});



$("#comissionmode_form").submit(function () {
$(".default").attr("disabled", true);
return true;
});


$("#redeembrandmaster_form").submit(function () {
$(".default").attr("disabled", true);
return true;
});

$("#countrymaster_form").submit(function () {
$(".default").attr("disabled", true);
return true;
});

$("#statemaster_form").submit(function () {
$(".default").attr("disabled", true);
return true;
});


$("#citymaster_form").submit(function () {
$(".default").attr("disabled", true);
return true;
});


$("#districtmaster_form").submit(function () {
$(".default").attr("disabled", true);
return true;
});


$("#subdistrictmaster_form").submit(function () {
$(".default").attr("disabled", true);
return true;
});


$("#subdistrictmaster_form").submit(function () {
$(".default").attr("disabled", true);
return true;
});



$("#servicemaster_form").submit(function () {
$(".default").attr("disabled", true);
return true;
});


$("#attribute_form").submit(function () {
$(".default").attr("disabled", true);
return true;
});

function get_base_url(this_obj) {
  base_url = this_obj.protocol+'//'+this_obj.hostname+':'+this_obj.port
  return base_url
}

function get_change_id(full_url)
 {
  str_reverse = full_url.split("")
  str_reverse = str_reverse.reverse()
  str_reverse = str_reverse.join("")
  id = str_reverse.split("/")[2]
  id = id.split("")
  id = id.reverse()
  id = id.join("")
  return id
}


$('#cashyfooddegradedcustomer_form input[name="_save"],#cashyfoodregularcustomer_form input[name="_save"],#cashyfoodgoldcustomer_form input[name="_save"],#resturantbranch_form input[name="_save"],#restaurantdetails_form input[name="_save"],#restaurantuser_form input[name="_save"],#menuimages_form input[name="_save"],#reservation_form input[name="_save"],#resturantmenu_form input[name="_save"],#actualwalletcoins_form input[name="_save"],#cashyuserredeem_form input[name="_save"],#cashycustomerwallet_form input[name="_save"],#contactdetails_form input[name="_save"],#cashyinvoice_form input[name="_save"],#refercode_form input[name="_save"],#ratingrecord_form input[name="_save"],#cashyuserpayment_form input[name="_save"],#notificationrecord_form input[name="_save"],#cashyuserotp_form input[name="_save"],#cashyfoodcustomer_form input[name="_save"]').attr('value','close');


$('#restaurantdetails_form input[name="_save"]').attr('value','update');



$(".field-customer_name a").click(function()
{
    test = this.href;
    base_url = get_base_url(this)
    if (/customercredit/i.test(test))
    {
      id = get_change_id(test)
      var newUrl = test.replace(test,base_url+"/wallet_admin/walletview/"+id)
      $(this).attr("href", newUrl); // Set herf value
    }
    else{
      $(this).attr("href", test);
    }
})


// $(".field-cashyUser a").click(function()
// {
//     test = this.href;
//     base_url = get_base_url(this)
//     if (/referralcredit/i.test(test))
//     {
//       id = get_change_id(test)
//       var newUrl = test.replace(test,base_url+"/refer_admin/referview/"+id)
//       $(this).attr("href", newUrl); // Set herf value
//     }
//     else{
//       $(this).attr("href", test);
//     }
// })

// $(".field-cashyUser a").click(function()
// {
//     test = this.href;
//     base_url = get_base_url(this)
//     if (/referralcredit/i.test(test))
//     {
//       id = get_change_id(test)
//       var newUrl = test.replace(test,base_url+"/refer_admin/referview/"+id)
//       $(this).attr("href", newUrl); // Set herf value
//     }
//     else{
//       $(this).attr("href", test);
//     }
// })


$("body.app-referralfriend.model-referral .field-cashyUser a").click(function()
{
  
    test = this.href;
    base_url = get_base_url(this)
    if (/referral/i.test(test))
    {
      id = get_change_id(test)
      var newUrl = test.replace(test,base_url+"/refer_admin/referralview/"+id)
      $(this).attr("href", newUrl); // Set herf value
    }
    else{
      $(this).attr("href", test);
    }
})


// $("body.app-cashyfooduser model-cashyfooddegradedcustomer .field-subscription_type nowrap").click(function()
// {
  
//     alert("HHHHHHHHHHHH")
//     test = this.href;
//     base_url = get_base_url(this)
//     if (/referral/i.test(test))
//     {
//       id = get_change_id(test)
//       var newUrl = test.replace(test,base_url+"/refer_admin/referralview/"+id)
//       $(this).attr("href", newUrl); // Set herf value
//     }
//     else{
//       $(this).attr("href", test);
//     }
// })









$('.sidebar-title .sidebar-title-acc').click(function(){
$(this).parent().parent().toggleClass('open');
});
var url = window.location.href;
var activePage = url;
$('.sidebar-section a').each(function () {
var linkPage = this.href;
if (activePage == linkPage) {
$(this).closest("div").parent().parent().addClass('open');
$(this).closest("div a").addClass("selected");
}
});



$("body.app-billmanagement model-billauthentication p").click(function()
{
    alert("ddddddddddddddd")
    test = this.href;
    base_url = get_base_url(this)
    if (/referral/i.test(test))
    {
      id = get_change_id(test)
      var newUrl = test.replace(test,base_url+"/refer_admin/referralview/"+id)
      $(this).attr("href", newUrl); // Set herf value
    }
    else{
      $(this).attr("href", test);
    }
})





  $(function () {
    "use strict";
    $(".app-billmanagement.model-billauthentication img, .m-popup-custom-image img").click(function () {
        var $src = $(this).attr("src");
        $(".show-img").fadeIn();
        $(".img-show img").attr("src", $src);
    });
    $(".img-show span, .overlay-img").click(function () {
        $(".show-img").fadeOut();
    });
});










});

















