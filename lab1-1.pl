студент('Маша', жен, отличник).
студент('Даша', жен, троечник).
студент('Геннадий', муж, хорошист).
студент('Иван', муж, отличник).

молодец(X, Y, _) :- студент(X, Y, отличник); студент(X, Y, хорошист).
