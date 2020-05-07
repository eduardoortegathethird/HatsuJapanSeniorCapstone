num=7

for folder in dataSet*
do
	cd $folder
	ls
	for pic in *.jpg
	do
		newPic="${num}_${pic}"
		echo "$newPic"
		cp $pic $newPic
		rm $pic
	done
	for xml in *xml
	do
		newXML="${num}_${xml}"
		echo "$newXML"
		cp $xml $newXML
		rm $xml
	done
	mv * ..
	cd ..
	let "num+=1"
	echo "$num"
	rm -rf $folder
done
