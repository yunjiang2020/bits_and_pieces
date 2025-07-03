
originalImage = getTitle();
run("8-bit");
run("Overlay Options...", "stroke=red width=1 fill=none set");
run("Median...", "radius=6");
run("Subtract Background...", "rolling=125 sliding");
run("Auto Threshold", "method=Default white");
roiManager("Reset");
run("Analyze Particles...", "pixel exclude clear add");

waitForUser("Select the image for nucleus area selection");
run("8-bit");

//run("Gaussian Blur...", "sigma=1");
//run("Subtract Background...", "rolling=125");

// Initialize arrays and variables
roiCount = roiManager("count");
positivePixelRatios = newArray();
intensityThreshold = 200;

// Loop through each ROI and calculate the positive pixel ratio
for (i = 0; i < roiCount; i++) {
    roiManager("select", i);
    
    // Get pixel statistics within the ROI
    getStatistics(area, mean, min, max, stdDev, histogram);

    // Calculate the number of pixels above the threshold
    positivePixelCount = 0;
    for (j = intensityThreshold + 1; j <= max; j++) {
        positivePixelCount += histogram[j];
    }

    // Calculate the total number of pixels in the ROI
    totalPixelCount = 0;
    for (j = 0; j < histogram.length; j++) {
        totalPixelCount += histogram[j];
    }

    // Calculate the ratio of positive pixels
    positivePixelRatio = positivePixelCount / totalPixelCount;
    positivePixelRatios[i] = positivePixelRatio;
}

// Print the ratios of positive signal pixels for each ROI
for (i = 0; i < roiCount; i++) {
    print(positivePixelRatios[i]);
}