# How to follow TSP guidelines

This file/document will be removed. It is meant to give some examples
of how to follow the TSP guidelines when extending the TSP.

NOTE:

- the examples below are just pseudocode to try to give a concrete
  feeling on how to implement the exploration/navigation features and
  follow the TSP guidelines. They are not meant to be seen as concrete
  proposals to extend/modify the existing TSP;
- the GET / POST methods are chosen just to be more RESTful (i.e. try
  to not use a POST when we do not create new resources)
- the parameters in the requests are always written as body params,
  just to make it easier to write. But they do not have to be body params.

## Timegraph states (a.k.a. intervals)

```
GET tsp/api/experiments/{expUUID}/outputs/timeGraph/{outputId}/states
{"parameters": 
  {"requested_timerange": 
    {"start": 111111111,
     "end": 222222222,
     "nbTimes": 1920}, // to follow "TSP guidelines", would it be better "precision"? or "samples"?
     "requested_items": [1,2] // to follow "TSP guidelines", would it be better "requested_row_ids"?
     }
}
```

## Filter rows of a timegraph

```
GET tsp/api/experiments/{expUUID}/outputs/timeGraph/{outputId}/states
{"parameters": 
  {"requested_timerange": 
    {"start": 111111111,
     "end": 222222222,
     "nbTimes": 1920}, // to follow "TSP guidelines", would it be better "precision"? or "samples"?
   "requested_row_labels": 
      [CPU0,CPU2]  // this is the label of the rows. How does the cli know about name of rows?
                   // The cli "asks" to the server about the labels of rows in the chart (e.g.
                   // from the timegraph/tree endpoint)
     }
}
```

## Filter states (a.k.a. intervals) of a timegraph chart

```
GET tsp/api/experiments/{expUUID}/outputs/timeGraph/{outputId}/states
{"parameters": 
  {"requested_timerange": 
    {"start": 111111111,
     "end": 222222222,
     "nbTimes": 1982}, 
   "requested_intervals": 
        [ThreadA*,FunctionB*,BankTransactionC*]
     }
}
```

## Filter states (a.k.a. intervals) of the chart with fullsearch

```
GET tsp/api/experiments/{expUUID}/outputs/timeGraph/{outputId}/states
{"parameters": 
  {"requested_timerange": 
    {"start": 111111111,
     "end": 222222222,
     "nbTimes": inf}, // or "max", however give the idea that we are trying to get all possible samples
   "requested_intervals": 
        [ThreadA*,FunctionB*]
     }
}
```

## Correlate components between charts (e.g. go-to-max)

An example of how to jump from a value in a table to the interval/state
that it represents in another chart.

First, ask some info to the table:

```
cli (ask): GET tsp/api/experiments/{expUUID}/outputs/<chart-type>/<chart-id>/tree
           {"parameters":{"requested_times":[0,100000000]}} // Side question: why is "requested_times" needed?
srv (ret): {"headers":[{Min},{Max},...], "entries" :[{1 sec},{2 min},...]}
```

In order to implement the "go-to-max" functionality, the client asks to the server
to return the "time series data" (in this case an interval) that was used to calculate
the value "2 min" at the table index 1,1:

```
cli (ask): GET tsp/api/experiments/{expUUID}/outputs/<chart-type>/<chart-id>/tree
           {"parameters":{"table_row": 1, "table_col":1]}}
srv (ret): {"data":[{"start": 1234, "end": 2345, "label": "ThreadA"}]}
```

The client uses than that info to "go to max" i.e. zoom in, filter or whaterver.
In theory it could also be possible to enable the server to "auto-align" other charts,
not sure if it is a good idea.

## Customize (e.g. select a subset of the input data to use to create a new chart)

Cli asks to the "time series input data" (e.g. the event table) to return some info on the input data:

```
cli (ask): GET tsp/api/experiments/{expUUID}/outputs/table/<chart-id>/columns
srv (ret): {"model":[{"name": "timestamp", "type":"number", ...}, {"name": "Device", "type":"string", ...}, ...]}
```

Cli asks to create a new statistics table using a subset of the input data.
The subset is selected using some of the previously returned params.

```
cli (ask): POST tsp/api/experiments/{expUUID}/outputs/<chart-type>
           {"parameters":{"outputId/chart-id":"my.custom.chart", "include":[{"Device": "CPU0"},...]}}
```
