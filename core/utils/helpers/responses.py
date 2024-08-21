from rest_framework import renderers
from rest_framework import status as status_code


class CustomRenderer(renderers.JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context["response"] if renderer_context else None
        status = response.status_code if response else None
        success = status in range(
            status_code.HTTP_200_OK, status_code.HTTP_300_MULTIPLE_CHOICES
        )

        formatted_data = {
            "status": status,
            "data": data if success else {},
            "success": success,
            "error": {},
        }

        if not success:
            exception = getattr(response, "data", {})
            if isinstance(exception, dict) and "detail" in exception:
                error_message = exception["detail"]
                if isinstance(error_message, str):
                    formatted_data["error"] = {"message": error_message}
                elif isinstance(error_message, list) and error_message:
                    formatted_data["error"] = {"messages": error_message}
                else:
                    formatted_data["error"] = {"detail": error_message}
            else:
                formatted_data["error"] = exception

        if "list" in data:
            formatted_data["data"] = data.get("list")
            pagination = {
                "total": data.get("total", len(data.get("list", []))),
                "num_pages": data.get("num_pages", 1),
                "current_page": data.get("current_page", 1),
                "count": len(data.get("list", [])),
            }
            formatted_data["pagination"] = pagination

        return super().render(formatted_data, accepted_media_type, renderer_context)


def formatPaginatedData(details):
    list_data, total, num_pages, current_page = details

    return {
        "list": list_data,
        "pagination": {
            "total": total,
            "num_pages": num_pages,
            "current_page": current_page,
            "count": len(list_data),
        },
    }
