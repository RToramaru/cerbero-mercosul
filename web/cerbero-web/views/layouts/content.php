<?php
/* @var $content string */

use yii\bootstrap4\Breadcrumbs;
?>

<?php if (Yii::$app->user->isGuest) { ?>
    <div class="mt-auto py-3 bg-light">
        <div class="content">
            <?= $content ?>
            <!-- /.container-fluid -->
        </div>
        <!-- /.content -->
    </div>
<?php } else { ?><div class="content-wrapper">
        <!-- Content Header (Page header) -->
        <div class="content-header">
            <div class="container-fluid">
                <div class="row mb-2">
                    <div class="col-sm-6">
                        <h1 class="m-0">
                            <?php
                            if (!is_null($this->title) && $this->title != 'principal') {
                                echo \yii\helpers\Html::encode($this->title);
                            }
                            ?>
                        </h1>
                    </div><!-- /.col -->
                    <div class="col-sm-6">
                        <?php
                        echo Breadcrumbs::widget([
                            'links' => isset($this->params['breadcrumbs']) ? $this->params['breadcrumbs'] : [],
                            'options' => [
                                'class' => 'breadcrumb float-sm-right'
                            ]
                        ]);
                        ?>
                    </div><!-- /.col -->
                </div><!-- /.row -->
            </div><!-- /.container-fluid -->
        </div>
        <!-- /.content-header -->

        <!-- Main content -->
        <div class="content">
            <?= $content ?>
            <!-- /.container-fluid -->
        </div>
        <!-- /.content -->
    </div>
<?php } ?>