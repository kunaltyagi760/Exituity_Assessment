import logging
import json
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ValuationRequestSerializer
from .steps.input_step import process_input
from .steps.validation_step import validate_data
from .steps.valuation_step import calculate_valuation
from .steps.output_step import generate_output
from .utils.logger import get_logger

logger = get_logger(__name__)

class RunValuationView(APIView):
    def post(self, request):
        try:
            # Initialize response logs
            logs = []
            
            # Step 1: Input Processing
            logger.info("Starting input processing")
            serializer = ValuationRequestSerializer(data=request.data)
            if not serializer.is_valid():
                return Response({
                    "status": "Failed",
                    "logs": ["Invalid input data"],
                    "errors": serializer.errors,
                    "timestamp": datetime.utcnow().isoformat()
                }, status=status.HTTP_400_BAD_REQUEST)
            
            input_data = process_input(serializer.validated_data)
            logs.append("Input received")
            
            # Step 2: Validation
            logger.info("Starting data validation")
            validation_result = validate_data(input_data)
            if not validation_result["is_valid"]:
                return Response({
                    "status": "Failed",
                    "logs": logs + ["Validation failed"],
                    "errors": validation_result["errors"],
                    "timestamp": datetime.utcnow().isoformat()
                }, status=status.HTTP_400_BAD_REQUEST)
            logs.append("Validation passed")
            
            # Step 3: Valuation
            logger.info("Starting valuation calculation")
            valuation_result = calculate_valuation(input_data)
            logs.append("Valuation completed")
            
            # Step 4: Output Generation
            logger.info("Generating final output")
            final_output = generate_output(valuation_result)
            logs.append("Report generated")
            
            # Return success response
            return Response({
                "status": "Success",
                "logs": logs,
                "result": final_output,
                "timestamp": datetime.utcnow().isoformat()
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            return Response({
                "status": "Failed",
                "logs": logs + [f"Internal error: {str(e)}"],
                "timestamp": datetime.utcnow().isoformat()
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)