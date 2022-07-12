// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "UObject/NoExportTypes.h"
#include "Style.generated.h"

/**
 * 
 */
UCLASS(BluePrintable)
class ASSIGNMENT2_API UStyle : public UObject
{
public:
	GENERATED_BODY()
	UPROPERTY(EditAnywhere)
	UClass* FloorPiece;
	UPROPERTY(EditAnywhere)
	UClass* WallPiece;
	UPROPERTY(EditAnywhere)
	UClass* CornerPiece;
	UPROPERTY(EditAnywhere)
	UClass* DoorPiece;
	
};
