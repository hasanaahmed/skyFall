function learnMoreYieldCurve(){
    var yieldCurve = "Yield curves outline the return an investor would receive for a US treasury bond. The yield curve maps the different returns that an investor would receive depending on how long they are willing to loan the government money. When the economy is healthy, longer term bonds will have a higher return which creates a positive slope in the yield curve. When the economy is about to enter a recession, shorter term bonds will have a higher return which creates a negative slope in the yield curve. This inverted yield curve occurs because investors have less faith in future prospects of the economy.";
    var yieldPara = document.getElementById("learnMoreYieldCurve");
    yieldPara.appendChild(document.createTextNode(yieldCurve));
    document.getElemtnById(learnMoreHousing).innerHTML = "";
    document.getElementById(learnMoreUnemployment).innerHTML = "";
}
function learnMoreHousing(){
    var housingPermits = "Building Permits for New Private Housing Units decrease prior to a recession because there are fewer investors interested in housing investments. Less investment in housing indicates that there is a declining demand for housing, which implies reduced consumer spending. This reduced consumer spending can lead to a recession.";
    var housingPara = document.getElementById("learnMoreHousing");
    housingPara.appendChild(document.createTextNode(housingPermits));
    document.getElemtnById(learnMoreYieldCurve).innerHTML = "";
    document.getElementById(learnMoreUnemployment).innerHTML = "";
}
function learnMoreUnemployment(){
    document.getElementById(learnMoreUnemployment).innerHTML = "While a lower unemployment rate may typically be associated with a stronger economy, a very low unemployment rate (loosely defined as below 4% in the USA) may also signal the imminent end of a bull market. This is because by the time the unemployment rate reaches this low point, the market has nearly reached maturity, growth is slowing, and interest rates are rising, which can ultimately lead to a recession.";
    document.getElementById(learnMoreYieldCurve).innerHTML = "";
    document.getElementById(learnMoreHousing).innerHTML = "";
}

            