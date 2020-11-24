# Test Tagger

### **Overview**

Tag all nodes that contain the word apple (using regex).


### **Parameters**

| **Parameter Name** | Default | Required? | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| tag_to_apply | RED | True | string | The tag that will be applied to the identified nodes |



### **Code Samples**

The following section provides an example of how you might use this cloud action in different languages.

#### YAML

The following is an example of how you register the action using YAML

```yaml
- name: Example Step
  ref: test-tagger
  options: {}
```

#### Python

The following is an example of adding the action to a Python pipeline

```python
pipeline = Pipeline.from_folder('/myfiles','*.*')
pipeline.add_step(RemoteAction(slug='{}', options={}, attach_source=False))
context = pipeline.run()

document = context.output_document
```

[Get Started with Python](https://developer.kodexa.com/developers/quick-starts/python-quick-start)

#### Java

The following is an example of adding the action to a Python pipeline

```java
Pipeline pipeline = Pipeline.fromFolder('/myfiles','*.*', false)
pipeline.addStep(new RemoteAction("{}",
                Options.start().set("tag_to_apply", "RED")
                ));
PipelineContext context = pipeline.run();

Document output = content.getOutputDocument();
```

[Get Started with Java](https://developer.kodexa.com/developers/quick-starts/using-kodexa-with-java-and-maven)