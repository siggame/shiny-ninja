#ifndef GETTERS_H 
#define GETTERS_H
#include "structures.h"

#ifdef _WIN32
#define DLLEXPORT extern "C" __declspec(dllexport)
#else
#define DLLEXPORT
#endif

#ifdef __cplusplus
extern "C" {
#endif

DLLEXPORT int moveGetId(_Move* ptr);
DLLEXPORT int moveGetFromFile(_Move* ptr);
DLLEXPORT int moveGetFromRank(_Move* ptr);
DLLEXPORT int moveGetToFile(_Move* ptr);
DLLEXPORT int moveGetToRank(_Move* ptr);
DLLEXPORT int moveGetPromoteType(_Move* ptr);


DLLEXPORT int pieceGetId(_Piece* ptr);
DLLEXPORT int pieceGetOwner(_Piece* ptr);
DLLEXPORT int pieceGetFile(_Piece* ptr);
DLLEXPORT int pieceGetRank(_Piece* ptr);
DLLEXPORT int pieceGetHasMoved(_Piece* ptr);
DLLEXPORT int pieceGetType(_Piece* ptr);



#ifdef __cplusplus
}
#endif

#endif
