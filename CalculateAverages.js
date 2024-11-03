function calculateAverage(dataArray) {
    if (!Array.isArray(dataArray) || dataArray.length === 0) {
        return null;
    }
    
    const sum = dataArray.reduce((acc, val) => acc + val, 0);
    return sum / dataArray.length;
}