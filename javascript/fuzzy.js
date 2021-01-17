function check_sol_as_fuzzyset (ans, sol) {

      // Create solution fuzzyset
      if (typeof sol == "string") {
        // The solution is a single
        solset = FuzzySet([sol])
      }
      else if (typeof sol == "object") {
        // Assume that we have a list
        solset = FuzzySet(sol)
      }
      else {
        // Error condition
        return {"is_error": true, "is_correct": true, "ratio": 0.0, "feedback": "Do not know"}
      }

      // Compare to fuzzyset
      matches = solset.get(ans)
      if (matches==null) {
        response = {"is_error": false, "is_correct": false, "ratio": 0.0, "feedback": "Seems incorrect"}
      }
      else {
        const [head, ...tail] = matches
        if (head==null) {
          response = {"is_error": false, "is_correct": false, "ratio": 0.0, "feedback": "Seems incorrect"}
        }
        else {
          const [ratio, matching] = head;
          response = {"is_error": false, "is_correct": true, "ratio": ratio, "feedback": "Seems correct"}
        }
    }

      return response
    }
