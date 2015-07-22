#!/bin/bash

GRINGO=/Users/nloira/install/gringo-3.0.5-source/build/release/bin/gringo
CLASP=clasp
UNCLASP=unclasp
HCLASP=hclasp

INSTANCE=$1
IREACTIONS="$INSTANCE/*.lp encodings/ireactions.lp"
EXPANSION="$INSTANCE/*.lp encodings/card_min_completions_all_targets.lp"
MINMAX="encodings/minmax.lp"
MINSUM="encodings/sum.lp"
MINCARD="encodings/card.lp"
HEURISTIC="encodings/heuristic.lp"

case $2 in
    opt1)
        $GRINGO $IREACTIONS | $CLASP --outf=1 | sed -e 's/ANSWER//g' | $GRINGO - $EXPANSION $MINCARD $MINSUM $MINMAX | $CLASP
        ;;
    opt4)
        $GRINGO $IREACTIONS | $CLASP --outf=1 | sed -e 's/ANSWER//g' | $GRINGO - $EXPANSION $MINCARD $MINMAX | $CLASP
        ;;
    opt5)
        $GRINGO $IREACTIONS | $CLASP --outf=1 | sed -e 's/ANSWER//g' | $GRINGO - $EXPANSION $MINCARD $MINSUM | $CLASP
        ;;
    opt8)
        $GRINGO $IREACTIONS | $CLASP --outf=1 | sed -e 's/ANSWER//g' | $GRINGO - $EXPANSION $MINCARD | $CLASP
        ;;
    1)
        if [ $# -ne 4 ] 
        then
            echo $"Usage: $0 INSTANCE_DIR 1 MINMAX MINSUM"
            exit 1
        fi
        $GRINGO $IREACTIONS | $CLASP --outf=1 | sed -e 's/ANSWER//g' | $GRINGO - $EXPANSION $HEURISTIC $MINSUM -c maxsum=$4 $MINMAX -c maxdist=$3 | $HCLASP -e record --opt-ignore 0
        ;;
    2)
        if [ $# -ne 5 ] 
        then
            echo $"Usage: $0 INSTANCE_DIR 2 MINMAX MINSUM MINCARD"
            exit 1
        fi
        $GRINGO $IREACTIONS | $CLASP --outf=1 | sed -e 's/ANSWER//g' | $GRINGO - $EXPANSION $MINCARD -c maxcard=$5 $MINSUM -c maxsum=$4 $MINMAX -c maxdist=$3 | $CLASP --opt-ignore 0
        ;;
    3)
        if [ $# -ne 3 ] 
        then
            echo $"Usage: $0 INSTANCE_DIR 3 MINMAX"
            exit 1
        fi
        $GRINGO $IREACTIONS | $CLASP --outf=1 | sed -e 's/ANSWER//g' | $GRINGO - $EXPANSION $HEURISTIC $MINMAX -c maxdist=$3 | $HCLASP -e record --opt-ignore 0
        ;;
    4)
        if [ $# -ne 4 ] 
        then
            echo $"Usage: $0 INSTANCE_DIR 4 MINMAX MINCARD"
            exit 1
        fi
        $GRINGO $IREACTIONS | $CLASP --outf=1 | sed -e 's/ANSWER//g' | $GRINGO - $EXPANSION $MINCARD -c maxcard=$4 $MINMAX -c maxdist=$3 | $CLASP --opt-ignore 0
        ;;
    5)
        if [ $# -ne 3 ] 
        then
            echo $"Usage: $0 INSTANCE_DIR 5 MINSUM"
            exit 1
        fi
        $GRINGO $IREACTIONS | $CLASP --outf=1 | sed -e 's/ANSWER//g' | $GRINGO - $EXPANSION $HEURISTIC $MINSUM -c maxsum=$3 | $HCLASP -e record --opt-ignore 0
        ;;
    6)
        if [ $# -ne 4 ] 
        then
            echo $"Usage: $0 INSTANCE_DIR 6 MINSUM MINCARD"
            exit 1
        fi
        $GRINGO $IREACTIONS | $CLASP --outf=1 | sed -e 's/ANSWER//g' | $GRINGO - $EXPANSION $MINCARD -c maxcard=$4 $MINSUM -c maxsum=$3 | $CLASP --opt-ignore 0
        ;;
    7)
        $GRINGO $IREACTIONS | $CLASP --outf=1 | sed -e 's/ANSWER//g' | $GRINGO - $EXPANSION $HEURISTIC | $HCLASP -e record 0
        ;;
    8)
        if [ $# -ne 3 ] 
        then
            echo $"Usage: $0 INSTANCE_DIR 8 MINCARD"
            exit 1
        fi
        $GRINGO $IREACTIONS | $CLASP --outf=1 | sed -e 's/ANSWER//g' | $GRINGO - $EXPANSION $MINCARD -c maxcard=$3 | $CLASP --opt-mode=ignore 0
        ;;
    *)
        echo $"Usage: $0 INSTANCE_DIR [opt1|opt4|opt5|opt8|1|...|8]"
        exit 1
esac
