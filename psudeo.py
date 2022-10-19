def process(self, inframe, outframe):
    img = inframe.getCvBGR()
    self.timer.start()
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    corners, ids, rej = cv2.aruco.detectMarkers(grayimg, self.dict, parameters=self.params)
    if ids is None:
        jevois.sendSerial('None {}')
    else :
        global centerCam
        global found
        xOffset = []
        allTvecs = []
        zDistance = []
        xzCoord = []
        xyCoord = []
        arcLengthDis = []
        arcDisbtwTag = []
        camArcDis = []
        camLocationY = []
        zTotal = 0
        arcTotal = 0

        if np.size(ids) > 0:  # If there are markers found by detector
            rvec, tvec, markerPoints = cv2.aruco.estimatePoseSingleMarkers(corners, markerSize, cameraMatrix=camMtx,
                                                                           distCoeffs=disCo)
            img = cv2.aruco.drawDetectedMarkers(img, corners, ids)
            # print('Picture: ', found)      #number of Pictures Found
            # found += 1
            # Extract just tvec for distance b/w tags
            allTvecs.append(tvec)
            arrayTvec = np.asarray(allTvecs[0])
            jevois.sendSerial('{}'.format(ids))
            jevois.sendSerial('tvec {}'.format(arrayTvec))
            jevois.sendSerial('done')
            # Create an array with (x,z) coordinates
            for i in range(0, len(arrayTvec)):
                xyCoord.append([arrayTvec[i, 0, 0], arrayTvec[i, 0, 1]])
            xyCoord = sorted(xyCoord, key=lambda x: x[0])  # Sort (x,y) coordinates from lowest x to highest
            xyCoord = np.asarray(xyCoord)

            for i in range(0, np.size(ids)):
                cv2.aruco.drawAxis(img, camMtx, disCo, rvec[i], tvec[i], markerSize)
                xOffset.append(tvec[i, 0, 0])  # Array to help find x closest to zero
                zDistance.append(tvec[i, 0, 2])
                yTag = tvec[i, 0, 1]
                yTag = round(yTag, 3)
                camLocationY.append(yTag)
                ##jevois.sendSerial('zDistance {}'.format(camLocationY))
                # print('x offset arrayinsi: ', xOffset)
                # print('ID: ', ID)
                # print('Distance: ', tvec[i, 0, 2])
                # print('X Coordinates: ', tvec[i, 0, 0])
                # print('tvec: ', tvec)
                # print('ids: ',ids)

        # Y distance for each tag
        # jevois.sendSerial('Y Distance {}'.format(camLocationY))
        # Average out the distance of z
        for i in range(len(zDistance)):
            zTotal += zDistance[i]
            # print('zTotal: ', zTotal)
        zTotal = round(zTotal / len(ids), 3)
        camLocationZ.append(zTotal)
        # jevois.sendSerial('z Distance average {}'.format(zTotal))

        # Find tag closest to 0, to find location of camera on x-axis
        xCloseZero = min(xOffset, key=abs)
        closestTag0 = np.where(xyCoord == xCloseZero)
        # print('clost tag 0: ', closestTag0)
        closestTag0 = np.asarray(closestTag0).flatten()
        closestTag0 = closestTag0[0]  # Array element value for tag on left side of center of camera

        # Origin tag is the far left tag
        # xLocationTag.append(xzCoord[0, 0])
        # jevois.sendSerial('orig {}'.format(xLocationTag[0]))
        # jevois.sendSerial('orig {}'.format(xzCoord[0, 0]))
        # print('closest tag pos', closestTag0Pos)
        # print('closest tag neg', closestTag0Neg)
        # print('origin tag1: ', xzCoord)
        # print('closest to 0 tag index value: ', closestTag0)
        # disBetweenTags = []

        originTag = xyCoord[0]

        # Distance from origin tag to each tag to the right
        # for j in range(0, len(xyCoord)) :
        #    jevois.sendSerial('orig {}'.format(xLocationTag[len(xLocationTag)-1]))
        #    xTag = abs(xLocationTag[len(xLocationTag)-1] - xzCoord[j, 0])
        #    xTag = round(xTag, 3)
        #    disBetweenTags.append(xTag)
        # disBetweenTags = np.asarray(disBetweenTags)
        # jevois.sendSerial('X distance of tag {}'.format(disBetweenTags))
        # print('Dis b/w 2 tags', disBetweenTags)
        # centerTag = disBetweenTags[closestTag0]        # Sets varible to origin tag distance to most centered tag
        # jevois.sendSerial('dis btw tag {}'.format(disBetweenTags))
        # print('dis b/w 2 tags: ', disBetweenTags)
        # Find where camera is relative to ArUco tags and puts location into array
        # camLocX = round(centerTag - xzCoord[closestTag0, 0], 3)
        # camLocationX.append(camLocX)
        # print('camLocation: ', camLocationX)
        # jevois.sendSerial('X distance of cam {}'.format(camLocX))
        outDiameter = 2 * tagHeight + diameter
        ratio = diameter / outDiameter
        arcLengthDis.append(0.0)
        for k in range(0, (len(xyCoord) - 1)):
            start = xyCoord[k]
            end = xyCoord[k + 1]
            curve = np.sum(np.sqrt(np.sum((end - start) ** 2)))
            print('curve = ', curve)
            curve = curve * calcRatio
            arcDisbtwTag.append(curve)

            arcTotal += curve
            arcLengthDis.append(arcTotal)
            # arcLengthDis.append(arcTotal)
            print('arcLengthDis = ', arcLengthDis)
        # jevois.sendSerial('arc length dis {}'.format(arcLengthDis))
        # jevois.sendSerial('curve btw tags {}'.format(arcDisbtwTag))
        for k in range(0, len(xyCoord)):
            if xyCoord[k, 0] > 0:
                start = xyCoord[k]
                end = centerCam
                print('start center = ', start)
                print('end center = ', end)
                curve = np.sum(np.sqrt(np.sum((start - end) ** 2)))
                curve = curve * calcRatio
                camArcDis.append(curve)
                print('camArcDis = ', camArcDis)
            elif xyCoord[k, 0] < 0:
                start = centerCam
                end = xyCoord[k]
                print('start = ', start)
                print('end = ', end)
                curve = np.sum(np.sqrt(np.sum((start - end) ** 2)))
                curve = curve * calcRatio
                camArcDis.append(curve)
                print('camArcDis = ', camArcDis)
        # jevois.sendSerial('cam x dist {}'.format(camArcDis))
        # cam location on pipe nneds fix
        if xyCoord[closestTag0, 0] > 0:
            camLocationX = arcLengthDis[closestTag0] + camArcDis[closestTag0]
        elif xyCoord[closestTag0, 0] < 0:
            camLocationX = camArcDis[closestTag0] - arcLengthDis[closestTag0]
        camLoc.append(camLocationX)
        print('cam loc pipe = ', camLoc)
        # jevois.sendSerial('X distance of cam {}'.format(camLocationX))

        fps = self.timer.stop()
        cv2.putText(img, fps, (3, img.shape[0] - 7), cv2.FONT_HERSHEY_SIMPLEX,
                    0.4, (255, 255, 255), 1, cv2.LINE_AA)
        outframe.sendCv(img)