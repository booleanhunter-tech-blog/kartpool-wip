async function displayNearbyStores(map, latitude, longitude) {
    const stores = await fetchNearbyStores(latitude, longitude);
    const storesGeoJson = convertToGeoJson(stores);
    plotStoresOnMap(map, storesGeoJson);
    return storesGeoJson;
}

function setStoreNavigation(map, storesGeoJson) {
  
}