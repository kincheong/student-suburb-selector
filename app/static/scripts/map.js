// CC stands for Campus Centre
const melbCentre = { lat: -37.9716929, lng: 144.7729589 }
const claytonCC = { lat: -37.9120327, lng: 145.1329772 }  
const caufieldCC = { lat: -37.8773481, lng: 145.0428116 }

const defaultBounds = {
    north: melbCentre.lat + 0.1,
    south: melbCentre.lat - 0.1,
    east: melbCentre.lng + 0.1,
    west: melbCentre.lng - 0.1,
}

let map             // the google map
let markers = []    // list of marker on the map
let geoCoder

// callback function when map js api is done loading
let initMap = () => {
    map = new google.maps.Map(document.getElementById("map"), {
        center: melbCentre,
        zoom: 12
    })
    geoCoder = new google.maps.Geocoder()
}

// get output suburb name from flask to geocode for setting map centre
let setCentreFromSuburbOutput = () => {
    let suburbName = document.getElementById("suburb-name")
    if (suburbName !== null) {
        suburbName = suburbName.innerText.slice(0, -1)  // get the output suburb name, remove the '!' at the end
        suburbName += " VIC"                                    // try limit search result within VIC
        geoCoder.geocode({address: suburbName, bounds: defaultBounds, region: "AU"}, (results, status) => {
            if (status === google.maps.GeocoderStatus.OK) {
                let topResult = results[0]                      // ideally, this should return the most relevant suburb in VIC
                let center = { lat: topResult.geometry.location.lat(),  lng: topResult.geometry.location.lng() }
                map.setCenter(center)
                map.setZoom(12)
            }
        })
        addMarkerFromAddress(suburbName)
    } else {
        map.setCenter(melbCentre)
        map.setZoom(8)
    }
}

// Add a marker at selected uni position
let addMarkerAtSelectedUni = () => {
    let university = document.getElementById("university")  // this is just the div container
    university = university.children[1].selectedOptions[0].outerText    // the uni name
    addMarkerFromAddress(university)
}

// Given an address, add a marker at that address
let addMarkerFromAddress = (address) => {
    geoCoder.geocode({address: address, bounds: defaultBounds, region: "AU"}, (results, status) => {
        if (status === google.maps.GeocoderStatus.OK) {
            let topResult = results[0]                      // ideally, this should return the most relevant suburb in VIC
            let address_latlng = { lat: topResult.geometry.location.lat(), lng: topResult.geometry.location.lng() }
            
            let marker = new google.maps.Marker({           // add marker
                position: address_latlng,
                map: map
            })
            marker.addListener("click", () => {
                map.panTo(marker.position)
            })
            markers.push(marker)
        }
    })
}

// Autocomplete is the search box of ggmap
let initAutocomplete = () => {
    const input = document.getElementById("autocomplete")
    const options = {
        bounds: defaultBounds,                       // set bounds for search result
        componentRestrictions: { country: "au" }     // limit result to just AU
    }

    const autocomplete = new google.maps.places.Autocomplete(input, options)
    autocomplete.addListener("place_changed", () => {       // fired when user enter the input or select the reccomended output
        let place = autocomplete.getPlace()
        if (place.geometry && place.geometry.location) {    // sometimes place dont have geometry nor location
            markers.push(new google.maps.Marker({           // add marker if possible 
                position: place.geometry.location,
                map: map
            }))
            map.panTo(place.geometry.location)
        }
    })
}

// One function call others init functions, or init some specific element
let initAll = () => {

    initMap()
    setCentreFromSuburbOutput()
    addMarkerAtSelectedUni()

    // let collBtn = document.getElementById("coll-btn")
    // let inputForm = document.getElementById("input-form")
    // collBtn.addEventListener("click", () => {
    //     if (inputForm.style.display === "block") {
    //         inputForm.style.display = "none"
    //     } else {
    //         inputForm.style.display = "block"
    //     }
    // })

}

window.initMap = initAll    // call this function when all HTML is loaded
