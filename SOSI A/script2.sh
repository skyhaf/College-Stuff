#!/bin/sh

echo "Hallo Kelas SOSI 2020-2021 Genap"
echo "Ini adalah $0"
echo "Jumlah Argumen: $#"
path=`pwd`
env=`printenv`

if [[ $# -gt 2 ]]
    then
    echo "List argumen:"
    echo "args 0 is $0"
    NAME=1
    for i in "$@"
    do
    echo "args $NAME is $i"
    (( NAME++ ))
    done
else
    echo "kurang"
fi

echo "Silakan masukkan sebuah kata"
read kataMasukkan


for (( i=1; i <= $1; i++))
do
    for ((j=1; j <= $2; j++))
    do
        echo "$kataMasukkan $i $j"
    done
done

echo "Silahkan pilih di antara opsi berikut:"
echo "1. Print current directory"
echo "2. Print current environment variable"
echo "- - - - - - - - - - - - - - - - - - - "
read pilihanMasukkan

if [[ $pilihanMasukkan == 1 ]]
    then
    echo "The current directory is:"
    echo $path
elif [[ $pilihanMasukkan == 2 ]]
    then
    echo "The environment variable are:"
    echo $env
else
    echo "Tidak tersediap opsi"
fi
