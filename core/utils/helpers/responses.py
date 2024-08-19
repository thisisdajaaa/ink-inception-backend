from rest_framework import renderers


class CustomRenderer(renderers.JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context["response"] if renderer_context else None
        status = response.status_code if response else None
        success = status in range(200, 300)

        # Handling pagination and data extraction generically
        pagination = data.pop("pagination", {})
        if "count" not in pagination:
            # Assume the main data is the remaining after popping pagination, or it's directly in 'data'
            main_data = (
                data if isinstance(data, list) else [data]
            )  # Ensure main_data is always a list
            pagination["count"] = len(main_data)
        else:
            main_data = list(data.values())[0] if data else []

        formatted_data = {
            "status": status,
            "data": main_data,
            "pagination": pagination,
            "success": success,
            "error": {},
        }

        return super().render(formatted_data, accepted_media_type, renderer_context)
